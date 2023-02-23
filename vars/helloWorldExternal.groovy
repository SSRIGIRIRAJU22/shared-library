def call(Map config = [:]) {
    loadLinuxScript(name: 'generate_pesh_passwords.py')
    sh "./generate_pesh_passwords.py -u <IBM id> -p <Password> --hmc <vHMC name with UVMID/SE> -r <multipleDay> [-f]"
}
