gen_data = document.querySelector('.gen-data')
pk = gen_data.getAttribute('value')

gen_data.addEventListener('click', function(){
  rows = document.querySelector('.rows').value
  dct = {
    'pk':pk,
    'rows':rows
  }
  
  json_dct = JSON.stringify(dct)
  // $.post("http://127.0.0.1:8000/create-file/",
  //   {
  //     "csrfmiddlewaretoken": getCookie("csrftoken"),
  //     json_dct,
  //   },
  //   console.log(json_dct)
  // );
  maket = document.querySelector('.files-maket')
  table_files = document.querySelector('.files-table')
  name_file = table_files.id
  id_maket = name_file + rows
  var is_file = true
  Array.from(table_files.children).forEach(function(f){
    // console.log(maket.id)
    if(f.classList.length == 1){
      console.log('1')
    if (id_maket == f.id){
      alert("Такой файл уже есть")
      is_file = false
    }}
  })
  if (is_file == true){
    
    $.post("http://127.0.0.1:8000/create-file/",
      {
        "csrfmiddlewaretoken": getCookie("csrftoken"),
        json_dct,
      },
      console.log(json_dct)
    );
    
      maket = maket.cloneNode(true);
      maket.classList.remove('hide')
      maket.classListk
      maket.id = id_maket
      maket.querySelector('.created').textContent = current_date()
      maket.querySelector('.download-link').href = 'http://127.0.0.1:8000/media/files/' + name_file + '.csv'
      table_files.append(maket)
      
      // url = 'http://127.0.0.1:8000/media/files/' + maket.id + '.csv' 
      // table_files.append(maket)
      // console.log(url)
      // files = document.querySelectorAll('.files')
    
      files = Array.from(document.querySelector('.files-table').children)
    console.log(files)
      files.forEach(function(file){
        if(file.classList.length == 1){
          name_file = file.id
          url = 'http://127.0.0.1:8000/media/files/' + name_file + '.csv' 
          console.log(file)
          check_file(url, file)
        }
    })

  }
})
files = document.querySelectorAll('.files')
files.forEach(function(file){
  name_file = file.id
  url = 'http://127.0.0.1:8000/media/files/' + name_file + '.csv' 
  check_file(url, file)
})

function current_date(){
  date = new Date()
  month = date.getMonth() + 1
  month = month.toString().padStart(2,0)
  day = date.getDate()
  day = day.toString().padStart(2,0)
  year = date.getFullYear()
  current_dat = `${day}-${month}-${year}`
  return current_dat
}

function check_file(url, fil) {
   $.ajax({
    type: 'HEAD',
    url: url,
    success: function() {
      console.log(fil)
      fil.querySelector('.status').textContent = 'Ready'
      fil.querySelector('.download').classList.remove('hide')
    },  
    error: function() {
      setTimeout(check_file(url, fil), 10000);
    }
})
}
// $.ajax({
//     type: 'HEAD',
//     url: 'http://127.0.0.1:8000/media/files/csv.csv',
//     success: function() {
//         console.log('hello')
//     },  
//     error: function() {
//         console.log('bye')
//     }
// });
