from typing import Literal
from teleport.exceptions import TeleportException

Shell = Literal["bash", "powershell"]


def activate(shell: Shell = "bash") -> str:
    if shell == "bash":
        return BASH_STR
    elif shell == "powershell":
        return PS_STR
    else:
        raise TeleportException(f"Shell {shell} not supported.")


BASH_STR = """\
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

PS_STR = """\
function tp {
    param(
        [Parameter(ValueFromRemainingArguments = $true)]
        [string[]]$Arguments
    )

    if ($Arguments.Count -eq 1) {
        $result = teleport get $Arguments[0]
        if ($LASTEXITCODE -eq 0) {
            Set-Location $result
        } else {
            Write-Host $result -ForegroundColor Red
            return $false
        }
    } else {
        teleport @Arguments
    }
}
"""
