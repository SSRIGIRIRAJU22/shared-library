def call(Map config = [:]) {
    //loadLinuxScript(name: 'generate_pesh_passwords.py')
    //loadLinuxScript(name: 'hello-world.py')
    loadLinuxScript(name: 'hello-world.sh')
    //sh "./generate_pesh_passwords.py -u ${config.username} -p ${config.password} --hmc ${config.HMCs} -r ${config.rtype} -f"
    sh './hello-world.sh'
}
