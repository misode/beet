#!tag "minecraft:load"

say begin foo

function demo:inner

#!function "demo:inner"
    #!tag "demo:custom"

    say begin inner

    #!for i in range(5)
        #!set nested_function = "demo:nested_" ~ i

        say calling {{ nested_function }}
        function {{ nested_function }}

        #!function nested_function
            #!tag "demo:nested"

            say from nested {{ i }}
        #!endfunction
    #!endfor

    say end inner
#!endfunction

say end foo
