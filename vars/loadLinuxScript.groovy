def call(Map config = [:]) { 
  def scriptcontents = libraryResource "scripts/generate_pesh_passwords.py"
  writeFile file: "${config.name}", text: scriptcontents 
  sh "chmod +x ${config.name}"
} 
