def call(Map config = [:]) {
    //loadLinuxScript(name: 'generate_pesh_passwords.py')
    //loadLinuxScript(name: 'hello-world.sh')
    //sh "./generate_pesh_passwords.py -u ${config.username} -p ${config.password} --hmc ${config.HMCs} -r ${config.rtype} -f"
    
    def scriptcontents = libraryResource "scripts/${config.name}"    
    writeFile file: "${config.name}", text: scriptcontents 
    sh "chmod +x ${config.name}"
    
    sh 'ls -ltr'
    sh './${config.name}'
}
