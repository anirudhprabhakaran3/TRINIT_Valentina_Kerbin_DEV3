package models

import (
	"errors"

	"golang.org/x/crypto/bcrypt"
	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	Username    string `json:"username" gorm:"unique"`
	Password    string `json:"password"`
	Age         uint   `json:"age"`
	Email       string `json:"email" gorm:"unique"`
	Name        string `json:"name"`
	AccountType bool   `json:"accounttype"`
}

func HashPassword(password string) (string, error) {
	bytes, err := bcrypt.GenerateFromPassword([]byte(password), 14)
	return string(bytes), err
}

func CheckPasswordHash(password, hash string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
	return err == nil
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

	password, err := HashPassword(user.Password)
	if err != nil {
		return nil, errors.New("password hashing error")
	}

	user.Password = password

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
