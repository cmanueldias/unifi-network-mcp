"""Tests for tool index behavior across registration modes."""

from __future__ import annotations

from src import tool_index


class TestToolIndexModes:
    """Verify get_tool_index behavior in lazy/meta_only and fallback scenarios."""

    def setup_method(self):
        """Reset global registry between tests."""
        tool_index.TOOL_REGISTRY.clear()

    def teardown_method(self):
        """Reset global registry between tests."""
        tool_index.TOOL_REGISTRY.clear()

    def test_lazy_mode_reads_manifest(self, monkeypatch):
        """Lazy mode should return the pre-generated manifest."""
        import src.bootstrap as bootstrap

        monkeypatch.setattr(bootstrap, "UNIFI_TOOL_REGISTRATION_MODE", "lazy")

        result = tool_index.get_tool_index()

        assert "tools" in result
        assert result["count"] == len(result["tools"])
        assert result["count"] >= 50
        assert any(tool["name"] == "unifi_list_clients" for tool in result["tools"])

    def test_meta_only_mode_reads_manifest(self, monkeypatch):
        """Meta-only mode should also return the pre-generated manifest."""
        import src.bootstrap as bootstrap

        monkeypatch.setattr(bootstrap, "UNIFI_TOOL_REGISTRATION_MODE", "meta_only")

        result = tool_index.get_tool_index()

        assert "tools" in result
        assert result["count"] == len(result["tools"])
        assert result["count"] >= 50
        assert any(tool["name"] == "unifi_list_devices" for tool in result["tools"])

    def test_fallback_to_registry_when_manifest_missing(self, monkeypatch):
        """When manifest is unavailable, tool index should fall back to runtime registry."""
        import src.bootstrap as bootstrap

        monkeypatch.setattr(bootstrap, "UNIFI_TOOL_REGISTRATION_MODE", "meta_only")

        monkeypatch.setattr(tool_index.Path, "exists", lambda self: False, raising=False)

        tool_index.register_tool(
            name="unifi_test_tool",
            description="Test tool",
            input_schema={"type": "object", "properties": {}},
            output_schema={"type": "object", "properties": {"success": {"type": "boolean"}}},
        )

        result = tool_index.get_tool_index()

        assert result["count"] == 1
        assert result["tools"][0]["name"] == "unifi_test_tool"
