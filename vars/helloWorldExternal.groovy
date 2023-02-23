def call(Map config = [:]) {
    loadLinuxScript(name: 'generate_pesh_passwords.py')
    sh "./${config.name} -u ${config.username} -p ${config.password} --hmc ${config.HMCs} -r ${config.rtype} -f"
}
