<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <div>
  <form action="/submit" id="userform" method="post">
  <p><strong>Title: </strong><input name="title" placeholder="Feature Title"required/></p>
  <p><strong>Description: </strong><input name="description" placeholder="Feature Description"required/></p>
  <p><strong>Client: </strong><select name="client" placeholder="Client">
    <option value='Client A'>Client A</option>
    <option value='Client B'>Client B</option>
    <option value='Client C'>Client C</option>
    <option value='Client D'>Client D</option>
  </select></p>
  <p><strong>Priority: </strong><select name="priority" placeholder="Priority"/>
    <option value= 1>1</option>
    <option value= 2>2</option>
    <option value= 3>3</option>
    <option value= 4>4</option>
    <option value= 5>5</option>
    <option value= 6>6</option>
    <option value= 7>7</option>
    <option value= 8>8</option>
    <option value= 9>9</option>
    <option value= 10>10</option>
  </select></p>
  <p><strong>Target Date: </strong><input name="targetdate" placeholder="Enter Date mm/dd/yyyy"required/></p>
  <p><strong>Product Area: </strong><select name="productarea" placeholder="Product Area">
    <option value='Policies'>Policies</option>
    <option value='Billing'>Billing</option>
    <option value='Claims'>Claims</option>
    <option value='Reports'>Reports</option>
  </select></p>
  <td><input type="submit" id="submit" value="Submit" class="button"></td>
</form>
</div>
<div>
    <h2 align="center">Current List of Feature Requests</h2> <BR><BR>
    <table border="0" style="width:50%; min-width:300px;" align="center">
    <tbody>
    <tr style="background:#333; color: white;">
        <th scope="col">Title</th>
        <th scope="col">Description</th>
        <th scope="col">Client</th>
        <th scope="col">Priority</th>
        <th scope="col">Target Date</th>
        <th scope="col">Product Area</th>
    </tr>
    {{!chart}}
    </tbody>
</div>
</body>
</html>
