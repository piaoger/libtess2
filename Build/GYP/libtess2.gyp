{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'libtess2',
      'type': 'static_library',
      'include_dirs': [
        '<@(include_dir_libtess2)',
        '.'
      ],
      'sources': [
        '<@(libtess2_sources)'
      ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions', '-g', '-O0' ],
      'conditions': [
        ['OS=="win"', {
          'defines': [
            'WIN32', 'UNICODE'
          ]
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '<@(include_dir_libtess2)'
        ],
      },
    }
  ]
}
