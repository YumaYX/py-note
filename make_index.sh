#!/bin/sh

printer () {
  echo ${@}
  echo
}

printer "# Menu)"

cd _codes
find . -type d | grep -v ^.$ | while read dir
do
  cd ${dir}
  printer "## $(basename ${dir})"
  
  find . | sort | grep '.py$' | while read line
  do
    script_name=$(basename ${line})
    output="${script_name}.markdown"
    
    echo "- [${script_name}](/py-note/${script_name}.html)"
    
    {
      md_file="${line%.*}.md"
      cat "${md_file}"
      echo;echo
      
      printer "## Code:"
      echo '```python'
      cat "${line}"
      printer '```'
      
      printer "## Output:"
      cmd="python3 ${line}"
      echo '```'
      ${cmd}
      printer '```'
      } > "./../../${output}"
    done
  echo
  cd ..
done
