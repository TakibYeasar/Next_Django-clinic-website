import { About, Banner, Doctors, Feature, Service, Testimonial } from '@/containers'
import Image from 'next/image'

export default function Home() {
  return (
    <>
      <Banner />
      <About />
      <Service />
      <Feature />
      <Doctors />
      <Testimonial />
    </>
  )
}
