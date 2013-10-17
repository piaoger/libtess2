
{
  'variables': {
    'include_dir_libtess2': [
      '../../Include'
    ],
    'include_dirs_example': [
      '../../Example',
      '../../Contrib/SDL/include',
      '../../Contrib'
    ],
    'nanosvg_sources': [
      '../../Contrib/nanosvg.h',
      '../../Contrib/nanosvg.c'
    ],
    'libtess2_sources': [
        '../../Source/bucketalloc.h',
        '../../Source/dict.h',
        '../../Source/geom.h',
        '../../Source/mesh.h',
        '../../Source/priorityq.h',
        '../../Source/sweep.h',
        '../../Source/tess.h',
        '../../Include/tesselator.h',

        '../../Source/bucketalloc.c',
        '../../Source/dict.c',
        '../../Source/geom.c',
        '../../Source/mesh.c',
        '../../Source/priorityq.c',
        '../../Source/sweep.c',
        '../../Source/tess.c'
    ],
    'lib_dir_sdl': [
        '../../Contrib/SDL/lib'
    ],
    'libs_gl': [
      'SDL.lib',
      'SDLmain.lib',
      'opengl32.lib'
    ]
  },
}
