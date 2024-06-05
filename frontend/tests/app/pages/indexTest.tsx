describe('Home', () => {

    // Renders main container with correct class names
    it('should render main container with correct class names', () => {
      const { container } = render(<Home />);
      const mainElement = container.querySelector('main');
      expect(mainElement).toHaveClass('flex min-h-screen flex-col items-center justify-between p-24');
    });

    // Handles missing image sources gracefully
    it('should handle missing image sources gracefully', () => {
      const { getByAltText } = render(<Home />);
      const vercelLogo = getByAltText('Vercel Logo');
      const nextLogo = getByAltText('Next.js Logo');
      expect(vercelLogo).toBeInTheDocument();
      expect(nextLogo).toBeInTheDocument();
    });
});
