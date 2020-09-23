{
    "targets": [
        {
            "target_name": "node-enet",
            "include_dirs": [
                "src",
                "lib/enet/include",
                "<!(node -e \"require('nan')\")"
            ],
            "sources": [
                "src/node-enet.h",
                "src/node-enet.c"
            ]
        }
    ]
}