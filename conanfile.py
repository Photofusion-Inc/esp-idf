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
        print("SOURCE: SYSTEM: " + osName)
        self.idf_install(osName)
        # self.idf_export(osName)
        self.run("setx CC \"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Auxiliary\\Build\\vcvarsall.bat\"")
        # self.run("setx CFLAGS \"\"")
        self.run("setx CXX \"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Auxiliary\\Build\\vcvarsall.bat\"")
        # self.run("setx CXXFLAGS \"-std=c++14\"")
        
        self.run("setx ASM \"C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\VC\\Auxiliary\\Build\\vcvarsall.bat\"")
        self.run("cd /D " + self.source_folder + os.sep + "esp-idf" + " & ." + os.sep + "export.bat & idf.py set-target esp32s2")

    def build(self):
        osName = platform.system()
        print("BUILD: SYSTEM: " + osName)
        # RUN EXPORT (every time, yes)
        self.idf_export(osName)

        # GO TO DIRECTORY
        # idf.py build
        self.run(self.source_folder + os.sep + "esp-idf" + os.sep + "." + os.sep + "export.bat & idf.py build")

    # def package(self):

        

    # def package_info(self):
        # self.cpp_info.libs = ["hello"]

    def idf_install(self, osName):
        if(osName == 'Windows'):
            print("EXECUTING ESP-IDF/INSTALL BAT IN: " + self.source_folder)
            self.run(self.source_folder + os.sep + "esp-idf" + os.sep + "install.bat")
        elif(osName == 'Linux' or osName == 'Darwin'): # linux or mac
            print("EXECUTING ESP-IDF/INSTALL SH IN: " + self.source_folder)
            self.run(self.source_folder + os.sep + "esp-idf" + os.sep + "." + os.sep + "install.sh")

    def idf_export(self, osName):
        if(osName == 'Windows'):
            print("EXECUTING ESP-IDF/EXPORT BAT IN: " + self.source_folder)
            self.run(self.source_folder + os.sep + "esp-idf" + os.sep + "." + os.sep + "export.bat")
        elif(osName == 'Linux' or osName == 'Darwin'): # linux or mac
            print("EXECUTING ESP-IDF/EXPORT SH IN: " + self.source_folder)
            self.run(". " + self.source_folder + os.sep + "esp-idf" + os.sep + "." + os.sep + "export.sh")

