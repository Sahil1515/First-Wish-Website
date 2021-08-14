https://stackoverflow.com/First_Wish_Main_Apps/48438575/call-django-on-html-button-click/48438962



Ways to call a django view when an event occurs:

# 1. Using javascript


```<input type="button" id='script' name="scriptbutton" value=" Run Script " onclick="goPython()">

    <script>
        function goPython() {
            $.ajax({
                url: "addToDatabase",
                context: document.body
            }).done(function () {
                alert('finished python script');;
            });
        }
    </script>
```
# 2. Using Simple tag
    <a class="btn btn-primary" href="{% url 'addToDatabase'%}">Delete>

# 3. Using Django Form
    <form action='addToDatabase' method='GET'>
        <button class="btn btn-primary" type='submit'> sort me</button>
    </form>


In all three cases you ahve to add a line in urls.py of the app

    path('addToDatabase', views.addToDatabase, name='addToDatabase')


## First visit or not

https://stackoverflow.com/First_Wish_Main_Apps/5004978/check-if-page-gets-reloaded-or-refreshed-in-javascript



   $(window).on('load', function () {
                alert("Hello")
                alert($("#dataAboutPage").val())
            });


# Pervent database population when page is refreshed in Django

In HTML

     <form action="addToDatabase" method="POST" id="prospects_form">
        {% csrf_token %}
        <input type="text" name='getName'>
        <input type="text" name="dataAboutPage" id='dataAboutPage' value="1">
        <button class="btn btn-primary" type="submit" id='dataAboutPage2'>Add data</button>
    </form>

In JQuery

    $("#dataAboutPage2").click(function () {
                $("#dataAboutPage").val("2")
            });


In view

    if(check!="1"):
            db.collection("Sahil").document().set({"Name": name})