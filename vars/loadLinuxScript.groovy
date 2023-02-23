def call(Map config = [:]) { 
  def scriptcontents = libraryResource "scripts/generate_pesh_passwords.py"
  writeFile file: "generate_pesh_passwords.py", text: scriptcontents 
  sh "chmod +x generate_pesh_passwords.py"
} 
