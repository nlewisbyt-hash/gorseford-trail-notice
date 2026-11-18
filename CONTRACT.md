# Gorseford Trail Notice — route book contract

This is a fictional HTTP route registry for Gorseford Trail Notice, an
invented municipal trail-status API. It is not a real service.

`compile_routes(routes)` takes a sequence of route dictionaries, each with
`name`, `method`, and `path`. It must satisfy every rule below.
`check_routes.py` is the authority. Do not edit the checker to make a
broken implementation pass.

1. `method` must be one of `GET`, `POST`, `PATCH`, or `DELETE`, written in
   uppercase. Any other method is an error.
2. Paths are normalized before comparison: a missing leading slash is added,
   and a trailing slash is stripped except when the path is `/`.
3. After normalization, the pair `(method, path)` must be unique.
4. Two routes that share a method conflict when, at the same path position,
   one has a static segment and the other has a `{param}` segment. Example:
   `GET /trails/featured` conflicts with `GET /trails/{id}`. Different
   methods do not conflict with each other on this rule.
5. A `{param}` name must match `[A-Za-z_][A-Za-z0-9_]*`. Hyphens and empty
   names are errors.
6. If a route is named `healthz`, it must be `GET /healthz` after
   normalization.
7. On success, return a tuple of compiled route dictionaries, each with
   `name`, `method`, and normalized `path`, sorted by path and then method.
8. Errors are raised as `RouteError`.
