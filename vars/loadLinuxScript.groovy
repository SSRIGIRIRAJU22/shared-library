def call(Map config = [:]) { 
  //def scriptcontents = libraryResource "scripts/generate_pesh_passwords.py"
  def scriptcontents = libraryResource "scripts/hello-world.py"
  writeFile file: "hello-world.py", text: scriptcontents 
  sh "chmod +x hello-world.py"
} 
