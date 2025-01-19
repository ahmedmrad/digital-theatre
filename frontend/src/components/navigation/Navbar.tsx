// src/components/navigation/Navbar.tsx
const Navbar = () => {
  return (
    <nav className="bg-gray-800 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <span className="text-xl font-bold">Digital Theatre</span>
          </div>
          <div className="flex space-x-4">
            <a href="/" className="hover:text-gray-300">Home</a>
            <a href="/plays" className="hover:text-gray-300">Plays</a>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;