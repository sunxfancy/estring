from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(username="sunxfancy")
    builder.add_common_builds(pure_c=False)
    builder.run()
