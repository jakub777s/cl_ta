I. Key functionalities of the application:
	1. Add task with selected title and status
	2. Show task list
	3. Filter task list based on task status
	4. Modify task status
	5. Delete task

II. Define 5 test cases covering functions of your choice:

	1. Test name: adding_uncompleted_task
	    
	    Top-level description of tested functionality
	    	This test case verify two functionalities. First is to add a task with selected title and status. Second is to show task list, which were previously added.
        Prerequisites (if needed)
        	None
        Steps to execute
        	1. Click "Add Task" button
        	2. Input value "/* car fixing */" in Title input in a new opened window
        	3. Status is set by default to "Incomplete"
        	4. Click "Add Task" button in the same window as Title input
        Validation criteria
        	1. Verify if a new popup is shown "Task added successfully" value
        	2. Verify if a new task was added to the list correctly:
        		- has it proper title,
        		- has it proper status,
        		- has it proper added time,
        		- has it delete/modify task button
       	
	2. Test name: adding_completed_task

		Top-level description of tested functionality
	    	This test case verify two functionalities. First is to add a task with selected title and status. Second is to show task list, which were previously added.
        Prerequisites (if needed)
        	None
        Steps to execute
        	1. Click "Add Task" button
        	2. Input value "¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿƒΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψωϑϒϖ•…′″‾⁄℘ℑℜ™ℵ←↑→↓↔↵⇐⇑⇒⇓⇔∀∂∃∅∇∈∉∋∏∑−∗√∝∞∠∧∨∩∪∫∴∼≅≈≠≡≤≥⊂⊃⊄⊆⊇⊕⊗⊥⋅⌈⌉⌊⌋⟨⟩◊♠♣♥♦"&<>ŒœŠšŸˆ˜–—‘’‚“”„†‡‰‹›€" in Title input in a new opened window
        	3. Set status to "Completed"
        	4. Click "Add Task" button in the same window as Title input
        Validation criteria
            1. Verify if a new popup is shown "Task added successfully" value
        	2. Verify if a new task was added to the list correctly:
        		- has it proper title,
        		- has it proper status,
        		- has it proper added time,
        		- has it delete/modify task button

	3. Test name: adding_task_with_empty_title
	    Top-level description of tested functionality
	    	This test case verify two functionalities. First is to add a task with selected title and status. Second is to show task list, which were previously added.
        Prerequisites (if needed)
        	None
        Steps to execute
           	1. Click "Add Task" button
        	2. Title input is empty in a new opened window
        	3. Status is set by default to "Incomplete"
        	4. Click "Add Task" button in the same window as Title input
        Validation criteria
        	1. Verify if a new popup is shown "Please enter a title" value
        	2. No new task has been added to the list (number of task at the list remains the same)
        

	4. Test name: cancel_adding_task_by_closing_form
	    Top-level description of tested functionality
	    	This test case verify two functionalities. First is to add a task with selected title and status. Second is to show task list, which were previously added.
        Prerequisites (if needed)
        	None
        Steps to execute
            1. Click "Add Task" button
        	2. Input value "check email" in Title input in a new opened window
        	3. Status is set by default to "Incomplete"
        	4. Click "Close" [X] button in the same window as Title input      
        Validation criteria
        	1. No new task has been added to the list (number of task at the list remains the same)

	5. Test name: cancel_adding_task_by_cancel_button
	    Top-level description of tested functionality
	    	This test case verify two functionalities. First is to add a task with selected title and status. Second is to show task list, which were previously added.
        Prerequisites (if needed)
        	None
        Steps to execute
            1. Click "Add Task" button
        	2. Title input is empty in a new opened window
        	3. Status is set by default to "Incomplete"
        	4. Click "Cancel" button in the same window as Title input      
        Validation criteria
        	1. No new task has been added to the list (number of task at the list remains the same)
