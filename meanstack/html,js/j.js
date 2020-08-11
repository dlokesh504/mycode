function handleb1(){
    var msg=document.getElementById("uid").value;

    alert("Welcome   "+msg);
}
function cal()
{

    var t=document.getElementById("numb").value;
    var t1=document.getElementById("numb2").value;

    t=Math.pow(t, t1);
    document.getElementById("result").value=t;



}