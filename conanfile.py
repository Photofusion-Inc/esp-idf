from conans import ConanFile
import os, platform

class EspIdfConan(ConanFile):
    name = "esp-idf"
    version = "4.2"
    license = "Apache 2.0"
    # author = "<Put your name here> <And your email here>"
    url = "https://github.com/Photofusion-Inc/esp-idf"
    description = "Conan packaging of esp-idf."
    topics = ("expressif", "esp32", "esp-idf")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        self.run("git clone --recursive https://github.com/Photofusion-Inc/esp-idf.git")
        osName = platform.system()
        print("SYSTEM: " + osName)
        if(osName == 'Windows'):
            print("EXECUTING ESP-IDF/INSTALL BAT IN: " + self.source_folder)
            self.run(self.source_folder + os.sep + "esp-idf" + os.sep + "install.bat")
            print("EXECUTING ESP-IDF/EXPORT BAT IN: " + self.source_folder)
            self.run(self.source_folder + os.sep + "esp-idf" + os.sep + "export.bat")
        elif(osName == 'Linux' or osName == 'Darwin'): # linux or mac
            print("EXECUTING ESP-IDF/INSTALL BAT IN: " + self.source_folder)
            self.run(self.source_folder + os.sep + "esp-idf" + os.sep + "." + os.sep + "install.sh")
            print("EXECUTING ESP-IDF/EXPORT BAT IN: " + self.source_folder)
            self.run(". " + self.source_folder + os.sep + "esp-idf" + os.sep + "." + os.sep + "export.sh")


        

    # def build(self):
        # cmake = CMake(self)
        # cmake.configure(source_folder="hello")
        # cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)


    # def package(self):

        

    # def package_info(self):
        # self.cpp_info.libs = ["hello"]

