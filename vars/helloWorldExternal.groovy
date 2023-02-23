def call(Map config = [:]) {
    loadLinuxScript(name: 'generate_pesh_passwords.py')
    //sh "./generate_pesh_passwords.py -u ${config.name} -p ${config.password} --hmc ${config.HMCs} -r ${config.rtype} -f"
    sh "./generate_pesh_passwords.py"
}
