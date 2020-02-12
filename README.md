# The Political Database

This project is about creating a CRUD application that is useable in the real world, so I decided to create a website whereby the the emphasis is on data collection. The idea behind the project is that users fill out the forms with information based on themselves, describing what party they will be voting for in the UK general election, this information includes a user comment giving the user an opportunity to tell other users why they are voting the way they are. This comment, with other demographic information can show what concerns people have that adhere from different social, economic, religious backgrounds have. But further, this information could be used to canvas opinions on behalf of parties  and could be used in research to see what correlations people have, for example 90% of the north east has higher wages and has a certain religious orientation and the reasons why this certain demographic will be voting for this party.

## UX

The website is aimed at people various  people, of whom may have multiple interests. First there are those who wish to have a say about why they are voting for this or that party. There maybe those who wish to learn more about the parties, that is why the first page has information on each of the main parties. 

![](C:\Users\Tom\Pictures\Screenshots\Screenshot (51).png)

The database was built in such away that it could be expanded upon for example wages have been set that £0-10000, 10001-20000 ect, but this could be expanded on simply by adding extra options to the database, therefor increasing the accuracy of the information this can be done to all demographic information including what parties people may wish to vote for. 



![](C:\Users\Tom\Pictures\Screenshots\Screenshot (50).png)





## Features

The nav-bar is an important feature and has been created using bootstrap. This means that the Navbar has been fixed to the top of the browsers page, thus giving access to all parts of the website at any point, through the use of anchor tags. The menu is a drop-down and so it takes up less space. Through the use of flask I have used url_for to allow easy navigation, and so should the template be changed you only have to change the template name and not the directory.

```
href="{{url_for('user_blogs')}}"
```

Another feature that has been used is the bootstrap 4 modal, this allows for lots of information to be displayed but at very little cost to browser retail. It also allows for a small amount of user interaction.

```html
 <div id="modal-conservative" class="modal" role="dialog">
                <div class="modal-dialog modal-lg">

                    <!-- Modal content-->
                    <div class="modal-content">

                        <div class="modal-header">
                            <h4 class="modal-title">Conservatives</h4>
                        </div>

                        <div class="container">

                            <div class="modal-body">
                                <p>The Conservative Party, officially the Conservative and Unionist Party, is a centre-right political party in the United Kingdom. The governing party since 2010, it is the largest in the House of Commons, with 288 Members
                                    of Parliament. It also has 234 members of the House of Lords, 4 members of the European Parliament, 31 Members of the Scottish Parliament, 11 members of the Welsh Assembly, 8 members of the London Assembly and 7,445
                                    local councillors.[13] The Conservative Party was founded in 1834 from the Tory Party—the Conservatives' colloquial name is "Tories"—and was one of two dominant political parties in the nineteenth century, along with
                                    the Liberal Party. Under Benjamin Disraeli it played a preeminent role in politics at the height of the British Empire. In 1912, the Liberal Unionist Party merged with the party to form the Conservative and Unionist
                                    Party. In the 1920s, the Labour Party surpassed the Liberals as the Conservatives' main rivals. Conservative Prime Ministers — notably Winston Churchill and Margaret Thatcher — led governments for 57 years of the twentieth
                                    century. Positioned on the centre-right to right of British politics, the Conservative Party is ideologically conservative. Different factions have dominated the party at different times, including one nation conservatives,
                                    Thatcherites, and liberal conservatives, while its views and policies have changed throughout its history. The party has generally adopted liberal economic policies—favouring free market economics, limiting state regulation,
                                    and pursuing privatisation—although in the past has also supported protectionism. The party is British unionist, opposing both Irish reunification and Welsh and Scottish independence, and historically supported the
                                    maintenance of the British Empire. The party includes those with differing views on the European Union, with Eurosceptic and pro-European wings. On social policy, it has historically taken a more socially conservative
                                    approach, though this has receded over recent decades. In foreign policy, it favours a strong military capability, being supportive of British participation in NATO. The Conservatives are a member of the International
                                    Democrat Union and the Alliance of Conservatives and Reformists in Europe, and sit with the European Conservatives and Reformists (ECR) parliamentary group. The Scottish, Welsh, Northern Irish and Gibraltarian branches
                                    of the party are semi-autonomous. Its support base consists primarily of middle-class voters, especially in rural areas of England, and its domination of British politics throughout the twentieth century has led to
                                    it being referred to as one of the most successful political parties in the Western world.[14][15][16]
                                </p>
                            </div>

                            <div class="modal-footer">
                                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>



```

A feature that has very much helped in the creation of this website is the redirect method. This has meant that when a function has been executed for example insert_blog the page automatically loads up another template, allowing for quick changes. 

```python
return redirect(url_for('user_blogs'))
```

 

### Future Features

Would include an authentication system, this is of highest priority as this would allow for much better interaction. Also this would also mean that users could only update and edit their own posts, allowing for greater security. I would most likely use WTForms for this.

Another major future feature would be the use of Mongodb Atlas graphs to represent the data shown in an aesthetically pleasing way.

A feature that would open up the database information would be to have a template page dedicated to the collection of the information whereby using database methods such as

## Technologies

-  JQuery  library- this allows for manipulation of the DOM speeding up the process of development, instead of using JavaScript 

- Flask

- Python3

- 

- Bootstrap 4 - this allows developers to create well organised websites that are easier to position the HTML elements. It has a number of features such as the grid-system, positioning, mobile-responsive and many more

     

## Testing

A HTML validator https://validator.w3.org/nu/#textarea has been used to validate the code.

The website has been tested for responsiveness using Google Chrome Development tools. 



## Deployment

Website was deployed using GitHub, to do this follow these instructions

1.  go to the GitHib repository  
2. under the repositories name click settings
3. go to GitHub pages (scroll down)
4. click on the drop-down menu under source and click on master branch
5. click save

the Website has also been deployed on Heroku

## Credits

Much credit has to go to the members of slack as without their patience in answering questions i would not of been able to do some of the things i have a done.

Credit has to go to the tutor team.

The images where all located on google images, to each of these un-named artists thank you.

A big thank you has to go to the online community stackoverflow, and W3schools who provided lots of information.





