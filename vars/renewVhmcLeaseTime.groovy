def call(Map config = [:]) {
    loadLinuxScript(name: 'renew_vhmc_lease_time.py')
    sh "./renew_vhmc_lease_time.py -u ${config.username} -p ${config.password} -n ${config.HMCs}"
}
