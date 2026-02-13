from operations import Operations
import api.server as server


def main():
    app = Operations()
    app.update_stats()
    server.app.run(debug=server.FLASK_DEBUG, port=server.FLASK_PORT) #Running with port 8000
    app.end_operation()
    print("Ohjelma suljetaan")
    return 0


#Switch
if __name__ == '__main__':
    main()