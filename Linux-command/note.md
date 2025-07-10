# pwd
- it shows present working directories

# cd 
- it use to change directiories

# ls
  
- here some syntax

        ls
              
              - it shows all file/folder in the current directoires as a list

        ls folderName/
  
              - it shows all file/folder in the folderName folder as a list
  
        ls / 
 
              - it shows all file/folder in the current directoires as a list

        ls -

             - it shows like ls
     
        ls ..

            - it takes one step back        

        ls -l

            - it give file as long format

        ls -a

            - it shows hidden files

        ls -al

            - it give long list with hidden file   

        ls -ls

            it shows long list with sorting

        ls folderName/*.*


            it shows all exntention file

        ls folderName/*.ext

            it shows specific extention file
        
        ls -ls > newFolder.txt

            it save ls content to newfolder. txt
        
        ls -d */

            it  list out all directories
        
- to know more about ls type man ls on terminal

# cd
- it used to change current directories
- syntax
    
        cd directory

        cd /

            it change directory to root
        
        cd -

            it mean home directory
        
        cd ..

            it mean parent directory 
        
        cd folderName

            It take to the mentioned folder
        
        cd first\ last or "first last"

            it is used to naviagte a folder which is separate by space

# cat

- it has 3 function
  - displaying text file
  - combining  copies of text file
  - creating new text file
- syntax

    - displaying 
  
            cat option file1 file2 etc

            cat fileName

                it display content of file 

            cat -b fileName

                it gives number on non-blank line

            cat -n fileName

                it gives number on all line
            cat -s fileName

                it makes many blank line to 1 blank line
            
            cat -E fileName

                it add $ sign in the end of every line
    
    - redirecting (output > file)


            cat > fileName 

                    it create new file and give option to write
            
            cat >> filename

                    it append content on the file
        
    - copying file


            cat fileName > file1Name 

# mkdir

- create new directory
- syntex


        mkdir folderName

        mkdir folderName/subFolder

            it create sub directory in existing folder
        
        mkdir -p folderName/subfolder

            it create new folder with sub folder
        
        mkdir -p folderName/{f1,f2,f3}
             it create multi sub folder in existing folder
# rmdir
- it remove directory if there is no file
- syntax
    

        rmdir folderName

            it remove folder if no file there
        
        rmdir -p folder/subfolder

            it remove folder with subfolder if no file there
        
        rm -r folder/subfolder

            it remove folder with subfolder even if there is file

# cp
- to copy one file to another
- syntax

        cp option source destination

        cp file1.txt file2.txt

            it copy content from file1.txt to file2.txt
        
        cp file.txt folderName

            it keep the file.txt to folderName
        
        cp -i file.txt file2.txt or folderName

            it show you if you want to overright or not
        
        cp -R dir1 dir2

            it copy one dir to another





            
            
            
