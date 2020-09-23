#include "node-enet.h"

NAN_MODULE_INIT(initModule) {
    enet_initialize()
}

NODE_MODULE(nodeEnet, initModule);