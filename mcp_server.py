import sys
import json
from client import TDPSOLA

psola = TDPSOLA()

def handle_call(name, arguments):
    if name == "stretch":
        sig = arguments["signal"]
        period = arguments["period"]
        factor = arguments.get("factor", 1.5)
        out = psola.time_stretch(sig, period, factor)
        return {"stretched_signal": out, "length": len(out)}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
