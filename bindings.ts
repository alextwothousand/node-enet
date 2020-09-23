let nodeEnet: NodeRequire;

if (process.env.DEBUG) {
    nodeEnet = require("/build/Debug/node-enet.node");
} else {
    nodeEnet = require("/build/Release/node-enet.node");
}

export { nodeEnet };