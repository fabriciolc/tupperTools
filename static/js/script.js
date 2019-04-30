$(document).ready(function(){   
    $("#RadioCheck").on('change', "input[name=typeOccurrence]", function() {  
        if($(this).val().toString() == 'Garantia'){
            $("#id_ocorrencia").prop('disabled','disabled');
            $("#id_ocorrencia").val('default');
            $("#id_ocorrencia").selectpicker("refresh");
        }else{
            $('#id_ocorrencia').prop('required','required');
            $("#id_ocorrencia").prop('disabled', false);
            $("#id_ocorrencia").selectpicker("refresh");
        }
    });
});