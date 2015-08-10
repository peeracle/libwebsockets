{
  'targets': [
    {
      'target_name': 'libwebsockets',
      'type': 'static_library',
      'standalone_static_library': 1,
      'sources': [
        'lib/base64-decode.c',
        'lib/handshake.c',
        'lib/libwebsockets.c',
        'lib/service.c',
        'lib/pollfd.c',
        'lib/output.c',
        'lib/parsers.c',
        'lib/context.c',
        'lib/sha-1.c',
        'lib/alloc.c',
        'lib/header.c',
        'lib/client.c',
        'lib/client-handshake.c',
        'lib/client-parser.c',
        'lib/ssl.c',
        'lib/server.c',
        'lib/server-handshake.c',
        'lib/extension.c',
        'lib/extension-deflate-frame.c',
        'lib/extension-deflate-stream.c',
      ],
      'dependencies': [
        '<(webrtc_depth)/third_party/zlib/zlib.gyp:zlib',
        '<(webrtc_depth)/third_party/boringssl/boringssl.gyp:boringssl'
      ],
      'include_dirs': [
        'config/<(OS)/<(target_arch)',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          'config/<(OS)/<(target_arch)',
        ],
      },
      'conditions': [
        ['OS == "win"', {
          'sources': [
            'lib/lws-plat-win.c',
          ],
          'msvs_settings': {
            'VCCLCompilerTool': {
              'WarnAsError': 'true',
              'DisableSpecificWarnings': ['4018']
            }
          }
        }, {
          'sources': [
            'lib/lws-plat-unix.c',
          ],
        }],
      ],
    },
  ],
}
