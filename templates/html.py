from languages import languages
import pandas as pd

for x in languages:
    jinja = '{{{{"checked='checked'" if ("{}" in selections ) else "" }}}}'.format(x)
    print(
        
        f'<label class="container">{x}<input type="checkbox" name="checkbox"  value="{x}" {jinja}/><span class="checkmark"></span></label>'
    )

# f'<input type="checkbox" name="checkbox"  value="{x}" {jinja} /><label>{x}</label><br>'

# <label class="container">AWS<input type="checkbox" name="checkbox"  value="AWS" {{"checked='checked'" if ("AWS" in selections ) else '' }}/><span class="checkmark"></span></label>

<label class="container">AWS<input type="checkbox" name="checkbox"  value="AWS" {{checked="checked" if ("AWS" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Bash/Shell<input type="checkbox" name="checkbox"  value="Bash/Shell" {{checked="checked" if ("Bash/Shell" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">C++<input type="checkbox" name="checkbox"  value="C++" {{checked="checked" if ("C++" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">COBOL<input type="checkbox" name="checkbox"  value="COBOL" {{checked="checked" if ("COBOL" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Cassandra<input type="checkbox" name="checkbox"  value="Cassandra" {{checked="checked" if ("Cassandra" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Clojure<input type="checkbox" name="checkbox"  value="Clojure" {{checked="checked" if ("Clojure" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Crystal<input type="checkbox" name="checkbox"  value="Crystal" {{checked="checked" if ("Crystal" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Delphi<input type="checkbox" name="checkbox"  value="Delphi" {{checked="checked" if ("Delphi" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Django<input type="checkbox" name="checkbox"  value="Django" {{checked="checked" if ("Django" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Drupal<input type="checkbox" name="checkbox"  value="Drupal" {{checked="checked" if ("Drupal" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">DynamoDB<input type="checkbox" name="checkbox"  value="DynamoDB" {{checked="checked" if ("DynamoDB" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Elasticsearch<input type="checkbox" name="checkbox"  value="Elasticsearch" {{checked="checked" if ("Elasticsearch" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Flask<input type="checkbox" name="checkbox"  value="Flask" {{checked="checked" if ("Flask" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Flow<input type="checkbox" name="checkbox"  value="Flow" {{checked="checked" if ("Flow" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Git<input type="checkbox" name="checkbox"  value="Git" {{checked="checked" if ("Git" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Go<input type="checkbox" name="checkbox"  value="Go" {{checked="checked" if ("Go" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Google Cloud Platform<input type="checkbox" name="checkbox"  value="Google Cloud Platform" {{checked="checked" if ("Google Cloud Platform" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Hadoop<input type="checkbox" name="checkbox"  value="Hadoop" {{checked="checked" if ("Hadoop" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Java<input type="checkbox" name="checkbox"  value="Java" {{checked="checked" if ("Java" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">JavaScript<input type="checkbox" name="checkbox"  value="JavaScript" {{checked="checked" if ("JavaScript" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Kubernetes<input type="checkbox" name="checkbox"  value="Kubernetes" {{checked="checked" if ("Kubernetes" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">LISP<input type="checkbox" name="checkbox"  value="LISP" {{checked="checked" if ("LISP" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">MariaDB<input type="checkbox" name="checkbox"  value="MariaDB" {{checked="checked" if ("MariaDB" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Microsoft Azure<input type="checkbox" name="checkbox"  value="Microsoft Azure" {{checked="checked" if ("Microsoft Azure" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Node.js<input type="checkbox" name="checkbox"  value="Node.js" {{checked="checked" if ("Node.js" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Oracle<input type="checkbox" name="checkbox"  value="Oracle" {{checked="checked" if ("Oracle" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">PHP<input type="checkbox" name="checkbox"  value="PHP" {{checked="checked" if ("PHP" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Pandas<input type="checkbox" name="checkbox"  value="Pandas" {{checked="checked" if ("Pandas" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Perl<input type="checkbox" name="checkbox"  value="Perl" {{checked="checked" if ("Perl" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">PowerShell<input type="checkbox" name="checkbox"  value="PowerShell" {{checked="checked" if ("PowerShell" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Python<input type="checkbox" name="checkbox"  value="Python" {{checked="checked" if ("Python" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Qt<input type="checkbox" name="checkbox"  value="Qt" {{checked="checked" if ("Qt" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">React.js<input type="checkbox" name="checkbox"  value="React.js" {{checked="checked" if ("React.js" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Redis<input type="checkbox" name="checkbox"  value="Redis" {{checked="checked" if ("Redis" in selections ) else "" }}/><span 
class="checkmark"></span></label>
<label class="container">Ruby on Rails<input type="checkbox" name="checkbox"  value="Ruby on Rails" {{checked="checked" if ("Ruby on Rails" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Rust<input type="checkbox" name="checkbox"  value="Rust" {{checked="checked" if ("Rust" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Scala<input type="checkbox" name="checkbox"  value="Scala" {{checked="checked" if ("Scala" in selections ) else "" }}/><span 
class="checkmark"></span></label>
<label class="container">Swift<input type="checkbox" name="checkbox"  value="Swift" {{checked="checked" if ("Swift" in selections ) else "" }}/><span 
class="checkmark"></span></label>
<label class="container">Terraform<input type="checkbox" name="checkbox"  value="Terraform" {{checked="checked" if ("Terraform" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">TypeScript<input type="checkbox" name="checkbox"  value="TypeScript" {{checked="checked" if ("TypeScript" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Unity 3D<input type="checkbox" name="checkbox"  value="Unity 3D" {{checked="checked" if ("Unity 3D" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Vue.js<input type="checkbox" name="checkbox"  value="Vue.js" {{checked="checked" if ("Vue.js" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">Xamarin<input type="checkbox" name="checkbox"  value="Xamarin" {{checked="checked" if ("Xamarin" in selections ) else "" }}/><span class="checkmark"></span></label>
<label class="container">jQuery<input type="checkbox" name="checkbox"  value="jQuery" {{checked="checked" if ("jQuery" in selections ) else "" }}/><span class="checkmark"></span></label>