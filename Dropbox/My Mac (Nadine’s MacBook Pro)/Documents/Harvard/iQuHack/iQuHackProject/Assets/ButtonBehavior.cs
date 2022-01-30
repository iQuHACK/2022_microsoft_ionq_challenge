using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor.Scripting.Python;
using UnityEditor;


public class ButtonBehavior : MonoBehaviour
{
	[MenuItem("Python Scripts/pythonconnector")]
	public static void pythonconnector()
	{
		PythonRunner.RunFile("Assets/new_python_script.py");
	}

}
