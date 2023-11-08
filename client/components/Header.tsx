import React from 'react';
import { FaArrowRight, FaClock, FaFacebook, FaHospital, FaInstagram, FaLinkedin, FaMapMarker, FaPhone, FaTwitter } from "react-icons/fa";

const Header = () => {
  return (
    <div className="">
      <div className="flex justify-between p-8 bg-secondary-color">
        <div className="flex">
          <div className="items-center flex ml-3 mr-3">
            <FaMapMarker className='text-primary-color text-lg ml-2 mr-2' />
            <small className='text-font-color text-base'>123 Street, New York, USA</small>
          </div>
          <div className="items-center flex contact">
            <FaClock className='text-primary-color text-lg ml-2 mr-2' />
            <small className='text-font-color text-base'>Mon - Fri : 09.00 AM - 09.00 PM</small>
          </div>
        </div>

        <div className="items-center flex">

          <div className="items-center flex contact">
            <FaPhone className='text-primary-color text-lg ml-2 mr-2' />
            <small className='text-font-color text-base'>+012 345 6789</small>
          </div>

          <a className="h-[2rem] w-[2rem] bg-font-light rounded-full ml-2 mr-2" href=""><FaFacebook className='text-xl text-primary-color m-2' /></a>
          <a className="h-[2rem] w-[2rem] bg-font-light rounded-full ml-2 mr-2" href=""><FaTwitter className='text-xl text-primary-color m-2' /></a>
          <a className="h-[2rem] w-[2rem] bg-font-light rounded-full ml-2 mr-2" href=""><FaLinkedin className='text-xl text-primary-color m-2' /></a>
          <a className="h-[2rem] w-[2rem] bg-font-light rounded-full ml-2 mr-2" href=""><FaInstagram className='text-xl text-primary-color m-2' /></a>
        </div>
      </div>

      <nav className="bg-bg-color p-8 flex justify-between items-center">
        <a href="/" className=" items-center">
          <h1 className='flex text-4xl font-bold'><FaHospital className='mr-2' />Klinik</h1>
        </a>

        <div className="flex items-center">
          <a href="/" className="mt-2 mb-2 ml-4 mr-4 text-font-color text-base font-medium uppercase outline-none no-underline active hover:text-primary-color">Home</a>
          <a href="/aboutus" className="mt-2 mb-2 ml-4 mr-4 text-font-color text-base font-medium uppercase outline-none no-underline hover:text-primary-color">About</a>
          <a href="/contact" className="mt-2 mb-2 ml-4 mr-4 text-font-color text-base font-medium uppercase outline-none no-underline hover:text-primary-color">Contact</a>
          <a href="/authenticate" className="mt-2 mb-2 ml-4 mr-4 text-font-color text-base font-medium uppercase outline-none no-underline hover:text-primary-color">Sign in</a>
          <a href="/registrations" className="mt-2 mb-2 ml-4 mr-4 text-font-color text-base font-medium uppercase outline-none no-underline hover:text-primary-color">Registration</a>
          <a href="/appointment" className="flex bg-primary-color text-font-light text-base font-medium uppercase outline-none no-underline p-6">Appointment <FaArrowRight className='pl-2 font-bold' /></a>
        </div>

      </nav>
    </div>
  )
}

export default Header