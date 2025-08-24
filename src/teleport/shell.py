def shell() -> str:
    bash_cmd = """\
tp() {
    if [ $# -eq 1 ]; then
        local result
        result="$(teleport get "$@")" 
        if [ $? -eq 0 ]; then
            cd "$result"
        else
            echo "$result"
            false
        fi
    else
        teleport $@
    fi
}
"""
    return bash_cmd
