"""Route registry for Gorseford Trail Notice (fictional fixture).

This file is intentionally broken. The planted issues are documented in
CONTRACT.md and asserted by check_routes.py. A correct fix changes this
module only.
"""

from __future__ import annotations


class RouteError(Exception):
    """Raised when a route cannot be compiled."""


ALLOWED_METHODS = {"GET", "POST", "PATCH", "DELETE", "PUT"}  # PUT is planted.


def _normalize(path):
    # Planted issue: trailing slashes are kept, so /trails and /trails/
    # look like different paths.
    if not path.startswith("/"):
        path = "/" + path
    return path


def compile_routes(routes):
    compiled = []
    seen = set()
    for route in routes:
        name = route["name"]
        method = route["method"]
        path = _normalize(route["path"])

        # Planted issue: PUT is accepted because it is in ALLOWED_METHODS.
        if method not in ALLOWED_METHODS:
            raise RouteError(f"unsupported method: {method}")

        key = (method, path)
        if key in seen:
            raise RouteError(f"duplicate route: {method} {path}")
        seen.add(key)

        # Planted issue: no static-versus-parameter conflict check.

        # Planted issue: a {param} name with a hyphen is accepted.
        # Planted issue: a route named healthz may use any method or path.

        compiled.append({"name": name, "method": method, "path": path})

    # Planted issue: sort by method only, not by path then method.
    compiled.sort(key=lambda item: item["method"])
    return tuple(compiled)
