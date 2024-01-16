'''Copyright 2024 Daniel Enders

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.'''

import os
from pkgutil import extend_path

versions = ['go1.18','go1.17','go1.16','go1.15','go1.14','go1.13','go1.12','go1.11','go1.10','go1.9','go1.8','go1.7','go1.6','go1.5','go1.4','go1.3','go1.2.2']
oses = ['windows', 'linux', 'darwin']
arches = ['amd64', '386']

for version in versions:
    print(version)
    myFile = open("hello.go", "w")
    myFile.write("package main\n")
    if version in ['go1.3','go1.2.2']:
        extend_path = 'pkg\\'
    else:
        extend_path = ''
    for dirpath, dirnames, filenames in os.walk("C:\\Users\\Daniel Enders\\sdk\\"+version+ "\\src\\"+extend_path):
        if (not 'testdata' in dirpath) and not 'internal' in dirpath and not 'vendor' in dirpath and not 'cmd' in dirpath and not dirpath.endswith('js') and not dirpath.endswith("runtime\\cgo"):
            count = 0
            for filenames in os.listdir(dirpath):
                if filenames.endswith('.go'):
                    if count:
                        temp = dirpath.split(os.sep)
                        if extend_path:
                            temp = temp[temp.index('pkg'):]
                        else:
                            temp = temp[temp.index('src'):]
                        temp = '/'.join(temp)
                        myFile.write('import _"'+temp[4:]+'"'+"\n")
                        break
                    else:
                        count+=1
    break
    myFile.write("\nfunc main() {\n return\n }")
    myFile.close()
    for ose in oses:
        os.environ['GOOS'] = ose
        for arch in arches:
            print(arch)
            if version in ['go1.4','go1.3','go1.2.2'] and arch == '386':
                version = version + '_86'
            os.environ['GOROOT'] = "C:\\Users\\Daniel Enders\\sdk\\" + version
            os.environ['GOTOOLDIR'] = "C:\\Users\\Daniel Enders\\sdk\\" + version + "\\pkg\\tool\\windows_amd64"
            os.environ['GOARCH'] = arch
            if os.system(version +' build -o ' + 'full_'+ose+'_'+arch+'_'+version):
                # myFile = open("hello.go", "w")
                # myFile.write("package main\n")
                # for dirpath, dirnames, filenames in os.walk("C:\\Users\\Daniel Enders\\sdk\\"+version+ "\\src\\"+extend_path):
                #     if (not 'testdata' in dirpath) and not 'internal' in dirpath and not 'vendor' in dirpath and not 'cmd' in dirpath and not dirpath.endswith('js') and not dirpath.endswith("runtime\\cgo"):
                #         count = 0
                #         for filenames in os.listdir(dirpath):
                #             if filenames.endswith('.go'):
                #                 if count:
                #                     temp = dirpath.split(os.sep)
                #                     if extend_path:
                #                         temp = temp[temp.index('pkg'):]
                #                     else:
                #                         temp = temp[temp.index('src'):]
                #                     temp = '/'.join(temp)
                #                     myFile.write('import _"'+temp[4:]+'"'+"\n")
                #                     break
                #                 else:
                #                     count+=1
                # myFile.write("\nfunc main() {\n return\n }")
                # myFile.close()
                print("FAIL")
                os.system(version +' build -o ' + 'empty_'+ose+'_'+arch+'_'+version)

            

