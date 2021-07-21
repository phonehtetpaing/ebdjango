<!-- temp function to show fields are disabled while using preset -->

let presetSelectField = document.querySelector("#preset");

presetSelectField.addEventListener('change',function(){
  checkPreset();
});

function checkPreset(){
  if(presetSelectField.value != "0"){
    isPreset = true;
  }else{
    isPreset = false;
  }
  toggleInputFields(isPreset)
}

function toggleInputFields(isPreset){
  var inputs = [].slice.call(document.querySelectorAll('input'));
  var selects = [].slice.call(document.querySelectorAll('select:not(#preset)'));
  console.log(isPreset)
  if(isPreset){
    inputs.forEach(input => disableField(input));
    selects.forEach(select=> select.style.opacity=0.7);
    function disableField(input){
        input.value = "#000";
        input.style.opacity=0.7;
    }
  }else{
    inputs.forEach(input => enableField(input));
    selects.forEach(select=> select.style.opacity=1);
    function enableField(input){
        input.style.opacity=1;
    }
  }
}

window.onload = function() {
  checkPreset();
};

<!-- todo: to preview colors in the field -->
// <!-- preset input -->
// let presetSelectField = document.querySelector("#preset");
// let chatBackgroundColor = document.querySelector("#--chatbackgroundcolor");
// let submitButtonColor = document.querySelector("#--submitbuttoncolor");
// <!-- END: preset input -->
// 
// <!-- preset value retrieval -->
// function getPresetValue(id) {
//     fetchPresetValuesFromAPI(id);
// }
// 
// function fetchPresetValuesFromAPI(id) {
//     $.ajax({
//         type: "GET",
//         url: "/contactchat/settings/get_presets/" + id,
//         processData: false,
//         contentType: false,
//         success: function (data) {
//             if (data.status === "match_not_found") {
//                 alert("Match not found. This doesn't appear to be a valid postal code.")
//             } else {
//                 setPresetValues(data.preset);
//             }
//         },
//         error: function() {
//             console.error('There was a connection error. Please try again.')
//         }
//     });
// }
// <!-- END: preset value retrieval -->
// 
// <!-- preview the preset -->
// presetSelectField.addEventListener('change',function(){
//   if(presetSelectField.value != 0){
//     checkPreview(presetSelectField.value)
//   }
// });
// 
// function checkPreview(preset_values){
//   getPresetValue(preset_values);
// }
// 
// function setPresetValues(preset_values){
//     var inputs = [].slice.call(document.querySelectorAll('input'));
//     var selects = [].slice.call(document.querySelectorAll('select:not(#preset)'));
//     inputs.forEach(input => disbleInput(input));
//     selects.forEach(select=> select.style.opacity=0.7);
//   // for (let i in preset_values) {
//   //   if (i === "chatbackgroundcolor") {
//   //     document.documentElement.style.setProperty(chatBackgroundColor.id, preset_values[i]);
//   //     console.log(preset_values[i]);
//   //     chatBackgroundColor.value=preset_values[i];
//   //   }
//   //   else if (i === "submitbuttoncolor"){
//   //     document.documentElement.style.setProperty(submitButtonColor.id, preset_values[i]);
//   //     console.log(preset_values[i]);
//   //     submitButtonColor.value=preset_values[i];
//   //   }
//   // }
//   // return true;
// }
// <!-- END: preview the preset -->

