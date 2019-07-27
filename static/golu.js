   
    $(document).ready(function(){
      
      $('.contentform').hide()
      $('#selecter').change(function(){
        if ($('#selecter option:selected').text()=='Index'){
          $('.contentform').show()

        }


      });

    });