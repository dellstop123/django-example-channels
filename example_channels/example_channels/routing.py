from channels.routing import route,ProtocolTypeRouter
from example.consumers import ws_connect, ws_disconnect


channel_routing = ProtocolTypeRouter([
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
])
