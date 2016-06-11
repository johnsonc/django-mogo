def modsettings(filepath, mode='normal'):
    s = open(filepath).read()
    if mode == 'collectstatic':
        s = s.replace(
                      "#STATIC_ROOT = os.path.join(BASE_DIR, 'static')\nSTATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)",
                      "STATIC_ROOT = os.path.join(BASE_DIR, 'static')\n#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)",
                      )
    else:
        s = s.replace(
                      "STATIC_ROOT = os.path.join(BASE_DIR, 'static')\n#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)",
                      "#STATIC_ROOT = os.path.join(BASE_DIR, 'static')\nSTATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)",
                      )
    f = open(filepath, 'w')
    f.write(s)
    f.close()
    return