def call(Map config = [:]) { 
  //def scriptcontents = libraryResource "scripts/generate_pesh_passwords.py"
  //def scriptcontents = libraryResource "scripts/hello-world.py"
  def scriptcontents = libraryResource "scripts/hello-world.sh"
  writeFile file: "hello-world.sh", text: scriptcontents 
  sh "chmod +x hello-world.sh"
} 
