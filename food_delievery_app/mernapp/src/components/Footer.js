import React from 'react'
import { Link } from 'react-router-dom'

export default function Footer() {
  return (
    <div className='bg-dark' style={{'color': 'white'}}>
      <footer className="footer mt-5 mb-0">
        <div className="container">
          <div className="row px-3">
            <div className="col-md-6 col-lg-3 mb-md-0 mb-4">
              <h2 className="footer-heading"><Link to="/" className="logo ms-0">CODEART7</Link></h2>
              <p>A Learning Portal for your Coding Interest.</p>
              <Link to="{% url 'about' %}" aria-label="Know more about us">Know more about us<i className="fa-solid fa-arrow-right m-0"></i></Link>
            </div>
            <div className="col-md-6 col-lg-3 mb-md-0 mb-4">
              <h2 className="footer-heading">What We Have</h2>
              <ul className="list-unstyled">
                <li><Link to="{% url 'blog-index' %}" className="py-1 d-block">Blogs</Link></li>
                <li><Link to="{% url 'codes-index' %}" className="py-1 d-block">Code Templates</Link></li>
              </ul>
            </div>
            <div className="col-md-6 col-lg-3 mb-md-0 mb-4">
              <h2 className="footer-heading">Links</h2>
              <ul className="list-unstyled">
                <li><Link to="/" className="py-1 d-block">Home</Link></li>
                <li><Link to="{% url 'terms' %}" className="py-1 d-block">Terms</Link></li>
                <li><Link to="{% url 'privacy' %}" className="py-1 d-block">Privacy Policy</Link></li>
                <li><Link to="{% url 'disclaimer' %}" className="py-1 d-block">Disclaimer</Link></li>
                <li><Link to="{% url 'copyright' %}" className="py-1 d-block">Copyright</Link></li>
              </ul>
            </div>
            <div className="col-md-6 col-lg-3 mb-md-0 mb-4">
              <h2 className="footer-heading">Subscribe</h2>
              <h2 className="footer-heading mt-5">Follow us on</h2>
              <div className="social-links">
                <Link aria-label="Twitter" to="https://twitter.com/RahulSi35649099" target="_blank" className="twitter"><i className="fa fa-twitter"></i></Link>
                <Link aria-label="Facebook" to="https://www.facebook.com/fb.official.codeart7/" className="facebook" target="_blank"><i className="fa fa-facebook"></i></Link>
                <Link aria-label="Instagram" to="https://www.instagram.com/official.codeart7/" className="instagram" target="_blank"><i className="fa fa-instagram"></i></Link>
                <Link aria-label="Youtube" to="https://www.youtube.com/@codeart7" className="youtube" target="_blank"><i className="fa fa-youtube"></i></Link>
                <Link aria-label="Linkedin" to="https://www.linkedin.com/company/codeart7/" className="linkedin" target="_blank"><i className="fa fa-linkedin"></i></Link>
              </div>
            </div>
          </div>
        </div>
        <div className="w-100 mt-5 border-top py-3">
          <div className="container">
            <div className="row px-3">
              <div className="col-md-6 col-lg-8">
                <p className="copyright m-0">
                  Copyright ©
                  <script>document.write(new Date().getFullYear());</script> All rights reserved &nbsp;| <Link
                    to="/"> &nbsp; Codeart7</Link>
                </p>
              </div>
            </div>
          </div>
        </div>
      </footer >
    </div >
  )
}
