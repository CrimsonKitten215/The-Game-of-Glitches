-- Table Creation
CREATE TABLE Choices (
    code varchar(4),
    name varchar(20),
    colour varchar(10),
    speech varchar(255),
    function varchar(10),
    choice_codes varchar(40),
    button_codes varchar(40)
);

CREATE TABLE Buttons (
    code varchar(4),
    display_text varchar(255),
    colour varchar(10)
);