def shell() -> str:
    bash_cmd = """\
tp() {
    if [ $# -eq 1 ]; then
        local result
        result="$(teleport get "$@")" && cd "$result"
    else
        teleport $@
    fi
}
"""
    return bash_cmd
