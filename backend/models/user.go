package models

import (
	"errors"

	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	Username    string `json:"username"`
	Password    string `json:"password"`
	Age         uint   `json:"age"`
	Email       string `json:"email"`
	Name        string `json:"name"`
	AccountType bool   `json:"accounttype"`
}

func InsertUser(
	username string,
	password string,
	age uint,
	email string,
	name string,
	accounttype bool,
) (*User, error) {
	user := User{
		Username:    username,
		Password:    password,
		Age:         age,
		Email:       email,
		Name:        name,
		AccountType: accounttype,
	}

	if res := DB.Create(&user); res.Error != nil {
		return nil, res.Error
	}
	return &user, nil
}

func FindUserbyUsername(username string) (*User, error) {
	var user User
	if res := DB.Where("username = ?", username).Find(&user); res.Error != nil {
		return nil, res.Error
	}

	if user.ID == 0 {
		return nil, errors.New("user does not exist")
	}

	return &user, nil
}

func FindUserByID(id uint) (*User, error) {
	var user User
	if res := DB.Find(&user, id); res.Error != nil {
		return nil, res.Error
	}
	return &user, nil
}
