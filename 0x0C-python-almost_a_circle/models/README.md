<!DOCTYPE html>
<html>
<body>
<h2>README for models</h2>
<h4>A directory within 0x0C-python-almost_a_circle.
A directory within the holbertonschool-higher_level_programming repo.</h4>

<table style="width:100%">
<tr>
<th>File Name</th>
<th>Description</th>
</tr>
<tr>
<td>__init__.py</td>
<td>An empty file to make this folder a Python module.</td>
</tr>
<tr>
<td>base.py</td>
<td>A class called <code>Base</code> that sets the public instance attribute <code>id</code> within the instantiation. It contains the private class attribute <code>__nb_objects</code> and has many json methods. This includes: <code>to_json_string</code>, <code>save_to_file</code>, <code>from_json_string</code>, <code>create</code>, and <code>load_from_file</code>.</td>
</tr>
<tr>
<td>rectangle.py</td>
<td>A class called <code>Rectangle</code> that inherits <code>Base</code>. It has an instantiation using the variables: <code>width</code>, <code>height</code>, <code>x</code>, <code>y</code>, and <code>id</code>. Each one but <code>id</code> are private instance attributes with their own getters and setters. These attributes can be updated at any time. There's also a <code>__str__</code> method, along with <code>area</code>, <code>display</code> that actually prints the instance, and <code>to_dictionary</code> prints the dictionary representation of <code>Rectangle</code>.</td>
</tr>
<tr>
<td>square.py</td>
<td>A class called <code>Square</code> that inherits <code>Rectangle</code>. It has an instantiation using the variables: <code>size</code>, <code>x</code>, <code>y</code>, and <code>id</code>. It calls it's super in order to set these variables, using <code>size</code> to represent <code>width</code> and <code>height</code>. This class contains a setter and getter for <code>size</code>. Any of these attributes can be updated at any time. There's also a dictionary representation of <code>Square</code>.</td>
</tr>
</table>

</body>
</html>